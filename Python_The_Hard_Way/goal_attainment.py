def calc_attainment(goal, bookings):
    attainment = bookings / goal * 100
    print(f"Current attainment = {attainment} %")

goal = float(input("What is your Goal?"))
bookings = float(input("What are the current bookings?"))
#goal = float(raw_goal)
#bookings = float(raw_bookings)

calc_attainment(goal, bookings)
