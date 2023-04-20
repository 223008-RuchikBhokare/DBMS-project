from django.http import HttpResponse
from django.shortcuts import render
from django.utils.text import normalize_newlines
from .models import Normdoctors, Normmedrec, Normpatients
from django.db import connections


def main(request):
    return render(request, "index.html")


def doctors(request):
    st = Normdoctors.objects.all()
    return render(request, "doctors.html", {"st": st})


def patients(request):
    st = Normpatients.objects.all()
    return render(request, "patients.html", {"st": st})


def medrec(request):
    st = Normmedrec.objects.all()
    return render(request, "medrec.html", {"st": st})


def insertdoctors(request):
    st = Normdoctors.objects.all()
    return render(request, "insertdoctors.html", {"st": st})


def insertdoctorsform(request):
    fields = [
        "id",
        "name",
        "age",
        "specialization",
        "salary",
        "patientid",
        "medicalrecordno",
    ]
    values = []
    for f in fields:
        values.append(normalize_newlines((request.GET.get(f, ""))))
    ip = Normdoctors(
        doc_id=values[0],
        doc_name=values[1],
        doc_age=values[2],
        specialization=values[3],
        salary=values[4],
        patient_id=values[5],
        mr_no=values[6],
    )
    ip.save()
    st = Normdoctors.objects.all()
    return render(request, "insertdoctors.html", {"st": st})


def insertpatients(request):
    st = Normpatients.objects.all()
    return render(request, "insertpatients.html", {"st": st})


def insertpatientsform(request):
    fields = [
        "patientid",
        "patientname",
        "age",
        "gender",
        "phoneno",
        "roomid",
        "registrationid",
        "prescriptionid",
        "billid",
        "medicalrecordno",
        "doctorid",
    ]
    values = []
    for f in fields:
        values.append(normalize_newlines((request.GET.get(f, ""))))
    ip = Normpatients(
        patient_id=values[0],
        p_name=values[1],
        age=values[2],
        gender=values[3],
        phone_no=values[4],
        room_id=values[5],
        reg_id=values[6],
        pres_id=values[7],
        bill_id=values[8],
        mr_no=values[9],
        doc_id=values[10],
    )
    ip.save()
    st = Normpatients.objects.all()
    return render(request, "insertpatients.html", {"st": st})


def insertmedrec(request):
    st = Normmedrec.objects.all()
    return render(request, "insertmedrec.html", {"st": st})

def insertmedrecform(request):
    fields = [
        "medicalrecordno",
        "treatment",
        "wbccount",
        "bloodgroup",
        "height",
        "weight",
        "doctorid",
        "patientid"
    ]
    values = []
    for f in fields:
        values.append(normalize_newlines((request.GET.get(f, ""))))
    ip = Normmedrec(
        mr_no=values[0],
        treatment=values[1],
        wbc_count=values[2],
        blood_group=values[3],
        height=values[4],
        weight=values[5],
        doc_id=values[6],
        patient_id=values[7]
    )
    ip.save()
    st = Normmedrec.objects.all()
    return render(request, "insertmedrec.html", {"st": st})

def delete(request):
    st = Normdoctors.objects.all()
    return render(request, "delete.html", {"st": st})

def deleteform(request):
    table = normalize_newlines((request.GET.get("table", "")))
    id = normalize_newlines((request.GET.get("id", "")))
    if table=="doctors":
        Normdoctors.objects.filter(doc_id=id).delete()
        st = Normdoctors.objects.all()
        return render(request, "doctors.html", {"st": st})
    elif table=="patients":
        Normpatients.objects.filter(patient_id=id).delete()
        st = Normpatients.objects.all()
        return render(request, "patients.html", {"st": st})
    elif table=="medrec":
        Normmedrec.objects.filter(mr_no=id).delete()
        st = Normmedrec.objects.all()
        return render(request, "medrec.html", {"st": st})
    
    
