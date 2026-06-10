def update_project_status(project):
    places = project.places.all()

    if places.exists() and all(p.visited for p in places):
        project.status = 'completed'
        project.save()