#	Facts
facts = {
"is_sunny": {"day1", "day3"},
"is_rainy": {"day2"},
"is_cloudy": {"day4"},
"is_weekend": {"day1", "day2"},
"is_weekday": {"day3", "day4"}, "is_holiday": {"day2"}
}


#	Rules
def go_for_walk(day):
return (day in facts["is_sunny"]) and (day in facts["is_weekend"])


def need_umbrella(day):
return (day in facts["is_rainy"]) or (day in facts["is_cloudy"])


def study(day):
return (day in facts["is_weekday"]) and (day not in facts["is_holiday"])


def relax(day):
return (day in facts["is_weekend"]) or (day in facts["is_holiday"])


def play_outdoor(day):
return (day in facts["is_sunny"]) and not need_umbrella(day)
 
def watch_movie(day):
return (day in facts["is_rainy"]) or (day in facts["is_holiday"])


# -------- Query Engine -------- def query():
days = {"day1", "day2", "day3", "day4"}
print("\nKnowledge Representation and Logic Programming – Activity Expert System\n") for d in days:
print(f"\nFor {d}:")
print(" Go for walk?		->", go_for_walk(d)) print(" Need umbrella? ->", need_umbrella(d)) print(" Study?	->", study(d))
print(" Relax?	->", relax(d))
print(" Play outdoor? ->", play_outdoor(d)) print(" Watch movie?	->", watch_movie(d))

#	Main
if  name	== " main ": query()
