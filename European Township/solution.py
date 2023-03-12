with open('ET_large.txt', 'r') as input_file, open('ET_large_output.txt', 'w') as output_file:
    # Read the number of townships
    T = int(input_file.readline())

    # Iterate over all townships
    for case in range(1, T+1):
        # Read the number of houses in the township and initialize totals
        N = int(input_file.readline())
        total_time = 0
        accent_paint = 0
        regular_paint = 0

        # Iterate over all houses in the township
        for i in range(N):
            # Read the details of the house
            details = input_file.readline().strip().split(',')
            H = int(details[0]) # Number of Victorian style halls
            S = int(details[1]) # Number of standard rooms
            R = int(details[2]) # Number of roof bed rooms

            # Calculate the number of walls in the house
            num_walls = H*6 + S*4 + R*3

            # Calculate the quantity of accent and regular paint required for each wall
            accent_qty = num_walls * 1.5 / 3
            regular_qty = num_walls * 2.25 / 3

            # Add the quantities to the totals
            accent_paint += accent_qty
            regular_paint += regular_qty

            # Calculate the time required to paint each wall and add it to the total time
            time = num_walls * (2.5/3 * accent_qty + 3.25/3 * regular_qty)
            total_time += time

        # Print the output for the township
        output_file.write("Case #%d: %.2f, %.2f, %.2f\n" % (case, total_time, accent_paint, regular_paint))