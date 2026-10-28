from django.shortcuts import render
from django.http import Http404

STUDENTS = [
    {"id": 1, "nom": "Aminata", "classe": "APD"},
    {"id": 2, "nom": "Moussa", "classe": "APD"},
    {"id": 3, "nom": "Fatou", "classe": "Informatique"},
    {"id": 4, "nom": "Awa", "classe": "Informatique"},
    {"id": 5, "nom": "Ibrahima", "classe": "APD"},
]

TEACHERS = [
    {"id": 1, "nom": "Mme Diallo", "matiere": "Mathématiques", "classe": "APD"},
    {"id": 2, "nom": "M. Ndiaye", "matiere": "Informatique", "classe": "Informatique"},
    {"id": 3, "nom": "Mme Ba", "matiere": "Français", "classe": "APD"},
    {"id": 4, "nom": "M. Sarr", "matiere": "Sciences", "classe": "Informatique"},
]

def home(request):
    return render(request, "students/home.html")

def about(request):
    return render(request, "students/about.html")

def student_list(request):
    classes = sorted({student["classe"] for student in STUDENTS})
    selected_class = request.GET.get("classe", "")
    if selected_class not in classes:
        selected_class = ""

    filtered_students = [
        student
        for student in STUDENTS
        if not selected_class or student["classe"] == selected_class
    ]
    context = {
        "students": filtered_students,
        "classes": classes,
        "selected_class": selected_class,
    }
    return render(request, "students/students_list.html", context)

def teacher_list(request):
    return render(request, "students/teachers_list.html", {"teachers": TEACHERS})

def student_detail(request, id):
    for student in STUDENTS:
        if student["id"] == id:
            context = {"student": student}
            return render(request, "students/student_detail.html", context)

    raise Http404("Étudiant introuvable")
