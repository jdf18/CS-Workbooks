# Career quote problem

QUOTES = {
  "engineer": "The engineer has been, and is, a maker of history.",
  "developer":
  "Logical thinking, passion and perseverance is the paint on your palette.",
  "analyst": "Seeing what other people can’t see gives you great vision.",
  None: "I'm sorry. We could not find a quote for your job."
}


def get_quote(job):
  if job.lower() in QUOTES.keys():
    print(QUOTES[job.lower()])
    return
  print(QUOTES[None])


get_quote(input())