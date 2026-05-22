def summarize_text(text):

    text = text[:1500]

    lines = text.split("\n")

    important_lines = []

    for line in lines:

        line = line.strip()

        if len(line) > 40:
            important_lines.append(line)

    summary = " ".join(important_lines[:5])

    return summary