north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))


north_count = north_int
south_count = south_int
east_count = east_int
west_count = west_int

south_north_total = north_count + south_count
east_west_total = east_count + west_count


while south_north_total + east_west_total > 0:
    if south_north_total >= east_west_total:
        if south_count > 5 and north_count > 5:
            south_count -= 5
            north_count -= 5
            south_north_total -= 10
            print("Green light on N/S")
        elif south_count > 5 and north_count < 5:
            south_count -= 5
            south_north_total -= north_count
            north_count -= north_count
            south_north_total -= 5
            print("Green light on N/S")

        elif south_count < 5 and north_count > 5:
            south_north_total -= south_count
            south_count -= south_count
            north_count -= 5
            south_north_total -= 5

            print("Green light on N/S")
        else:
            south_north_total -= south_count
            south_north_total -= north_count
            south_count -= south_count
            north_count -= north_count

            print("Green light on N/S")



    else:
        if west_count > 5 and east_count > 5:
            west_count -= 5
            east_count -= 5
            east_west_total -= 10
            print("Green light on E/W")
        elif west_count > 5 and east_count < 5:
            west_count -= 5
            east_west_total -= east_count
            east_count -= east_count
            east_west_total -= 5
            print("Green light on E/W")

        elif west_count < 5 and east_count > 5:
            east_west_total -= west_count
            east_count -= 5
            west_count -= west_count
            east_west_total -= 5
            print("Green light on E/W")
        else:
            east_west_total -= east_count
            east_west_total -= west_count
            east_count -= east_count
            west_count -= west_count
            print("Green light on E/W")



else:
    print("No cars waiting, the traffic jam has been solved!")