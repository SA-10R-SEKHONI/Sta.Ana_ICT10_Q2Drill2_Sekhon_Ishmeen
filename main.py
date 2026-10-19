from pyscript import document

#members for each grade level.
grade_7 = {
    "Virk Eknoor", "Abuiza Kiehla", "Maria Graciella"
}

grade_8 = {
    "Gill Sargunn", "Levine Abby", "Gambol Lily", "Castro Daphne"
}

grade_9 = {
    "Cuevas Mikaela", "Jarlego Zoe", "Lal Dhia", "Paredes Roux"
}

grade_10 = {
    "Sekhon Ishmeen", "Osea Eleanor", "America Erin"
}

# Connect each grade level to its set.
grade_sets = {
    "Grade 7": grade_7,
    "Grade 8": grade_8,
    "Grade 9": grade_9,
    "Grade 10": grade_10,
}

def update_results():
    # Combine the four sets into one master set.
    all_members = grade_7 | grade_8 | grade_9 | grade_10

    # Member names format
    member_lines = "<br>".join(
        map(lambda name: f"🏐 {name}", sorted(all_members))
    )

    # Total using an f-string.
    document.getElementById("results").innerHTML = f"""
        <div class="roster-title">ALL MEMBERS</div>
        <div class="member-list">{member_lines}</div>
        <div class="total">
            <span>Total members</span>
            <span class="total-number">{len(all_members)}</span>
        </div>
    """

def add_member(event=None):
    # Input boxes and selected grade.
    first_name = document.getElementById("first-name").value.strip()
    last_name = document.getElementById("last-name").value.strip()
    selected_grade = document.getElementById("grade-level").value

    # Combine the first and last names.
    full_name = f"{first_name} {last_name}".strip()

    # Adding the member to the selected grade set.
    grade_sets[selected_grade].add(full_name)

    document.getElementById("message").innerText = (
        f"Submitted: {full_name} — {selected_grade}. "
        "The roster has been updated."
    )

    update_results()

update_results()
