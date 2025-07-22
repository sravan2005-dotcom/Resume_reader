from django.shortcuts import render,redirect
from .forms import ResumeForm
from .models import Resume
from .utils import check_eligibility

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            # After saving, check eligibility
            eligibility = check_eligibility(resume.resume_file)
            resume.eligibility_status = eligibility
            resume.save()
            return redirect('result', resume_id=resume.id)
    else:
        form = ResumeForm()
    return render(request, 'upload_resume.html', {'form': form})

def result(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    return render(request, 'result.html', {'resume': resume})


