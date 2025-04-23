# from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import JsonResponse
from .models import Visitor

def visitor_list(request):
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    visitors = Visitor.objects.all()
    
    # Apply date filtering if both dates are provided
    if start_date and end_date:
        visitors = visitors.filter(datetime__date__range=[start_date, end_date])

    return render(request, "visitor_list.html", {"visitors": visitors})

def update_approval(request, visitor_id, status):
    visitor = get_object_or_404(Visitor, id=visitor_id)
    
    if status in [0, 1]:  # Ensure valid status
        visitor.approval = status
        visitor.save()
        return JsonResponse({"success": True, "message": "Approval status updated!"})
    
    return JsonResponse({"success": False, "message": "Invalid status!"})
