# weight = 4.8 lbs
weight = 41.5 lbs

# calculating for ground shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
  print("It will cost £", cost_ground, "by Ground Shipping")
elif weight > 2:
  cost_ground = weight * 3.0 + 20
  print("It will cost £", cost_ground, "by Ground Shipping")
elif weight > 6:
  cost_ground = weight * 4.0 + 20
  print("It will cost £", cost_ground, "by Ground Shipping")
elif weight > 10:
  cost_ground = weight * 4.75 + 20
  print("It will cost £", cost_ground, "by Ground Shipping")

  # calculating for ground shipping premium
cost_ground_prem = 125.0
print("The flat rate for Ground Shipping Premium is £", cost_ground_prem)

# calculating for drone shipping
if weight <= 2:
  cost_drone = weight * 4.5
  print("It will cost £", cost_drone, "by Drone Shipping")
elif weight > 2:
  cost_drone = weight * 9.0
  print("It will cost £", cost_drone, "by Drone Shipping")
elif weight > 6:
  cost_drone = weight * 12.0
  print("It will cost £", cost_drone, "by Drone Shipping")
elif weight > 10:
  cost_drone = weight * 14.25
  print("It will cost £", cost_drone, "by Drone Shipping")

# this will tell the customer what the cheapest delivery type is based on the package weight.
if cost_ground < cost_drone and cost_ground < cost_ground_prem:
  print("The cheapest method of delivery is by Ground Shipping at £", cost_ground)
if cost_drone < cost_ground and cost_drone < cost_ground_prem:
  print("The cheapest method of delivery is by Drone Shipping at £", cost_drone)
if cost_ground_prem < cost_ground and cost_ground_prem < cost_drone:
  print("The cheapest method of delivery is by Ground Shipping Premium at £", cost_ground_prem)
