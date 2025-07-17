import os

def generate_invitations(template, attendees):
    # Type checking
    if not isinstance(template, str):
        print(f"Error: Expected 'template' to be a string, got {type(template).__name__} instead.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Expected 'attendees' to be a list of dictionaries.")
        return

    # Empty input checks
    if template.strip() == "":
        print("Error: Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        content = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            content = content.replace(f"{{{key}}}", str(value) if value else "N/A")

        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")
