# Convertion from Pounds (lbs) to Kilogram (kg)
weight_in_pounds = float(input("Weight in Pounds (lbs): "))
dividend = 2.205
kg = float(weight_in_pounds) / float(dividend)
print("Weight converted to Kilogram:","{:,.2f}".format (kg))

#===========================================================================

print("===========================================================================")

# Convertion from Miles (mi) to Kilometer (km)
length_in_miles = float(input("Length in Miles (mi): "))
dividend = 1.609
km = float(length_in_miles) / float(dividend)
print("Length converted to Kilometer (km):","{:,.2f}".format (km))

#===========================================================================

print("===========================================================================")

# Convertion from Farenheit (°F) to Cesius (°C)
temperature_in_farenheit = float(input("Temperature_in_Farenheit (°F): "))
# Farenheit to Cesius formula  (32°F − 32) × 5/9 = °C
celsius = float(temperature_in_farenheit - 32) * float(5 / 9)
print("Temperature converted to Celsius (°C):","{:,.2f}".format (celsius))

#===========================================================================

print("===========================================================================")

# For age input
student = 10
# Storage para sa summation ng lahat
studenttotal = 0
for i in range(student):
    studentage = float(input("Student " + str(i+1) + ": "))
    studenttotal += studentage
student_age_ave = studenttotal / student
print("Student Age Average:", student_age_ave)

#===========================================================================

print("===========================================================================")

# Characters
Prota1 = "Malin Is"
Prota2 = "Anne Dumi"
SideChar1 = "Kut Silyu"
SideChar2 = "Jas Wa"
SideChar3 = "Lakay Jurds"
SideChar4 = "Kut Sinta"

# Story
story = f"{Prota1}, the Troll,\nA Fantasy Novel\nby Joayde Paul E. Padilla Jr.\n\n"

story += f"In a house there lived a peaceful, magical, fluffy troll named {Prota1}. A snowy beautiful, wobbly house, filled with spells and solid walls, or yet a ruddy, pretty, quiet house with nothing in it to sit on or to eat; it was a troll-house, and that means comfort. One day, after a troubling visit from the ogre {Prota2}, {Prota1} left her house and set out in \nsearch of three sunny charms. A quest undertaken in the company of a human named {SideChar2}, a little fairy named {SideChar4}, and windy old folk {SideChar3}.\n"

story += f"In the search for the ogre-guarded charms, {Prota1} surprises even herself with her strength and skill as a mage. During her travels, {Prota1} rescues a Knife, but not just any other knife; it was {SideChar1}, a reincarnated man as a knife, an heirloom that belongs to {Prota2}. But when Anne refused to sing after their mini reunion, their friendship is over. \nHowever, {Prota2} is wounded at the Battle of Blenheim, and the two reconcile just after {Prota1} engages in some serious battling and saves {Prota2}. {Prota1} accepts one of the three sunny charms and returns home to her house a very wealthy troll.\n"

print(story)