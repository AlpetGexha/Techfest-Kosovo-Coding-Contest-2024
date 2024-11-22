def calculate_total_voltage(adapter_ratings, port_voltages):
    # Parse the adapter ratings and port voltages
    adapters = sorted(adapter_ratings)
    ports = sorted(port_voltages, reverse=True)

    # Determine the motorcycle's built-in charger voltage
    highest_adapter = max(adapters)
    motorcycle_voltage = highest_adapter + 3

    total_voltage = 0
    used_ports = set()

    # Match adapters to ports
    for adapter in adapters:
        for port in ports:
            if port not in used_ports and port <= adapter:
                total_voltage += adapter + port
                used_ports.add(port)
                break

    # Find the highest available port for the motorcycle
    for port in ports:
        if port not in used_ports:
            total_voltage += motorcycle_voltage + port
            break

    return total_voltage


adapter_ratings = [26,21,41,44,9,82,70,11,14,28,87,42,92,15,18,6,100,16,72,46,13,8,94,45,1,99,40]
port_voltages = [11,95,100,84,87,77,25,46,36,93,49,32,52,9,5,94,54,78,68,8,90,65,75,24,88,45,40,80,14,28,83,73,82,27,1,91,96,34,4,50,89,16,63,17,60,38,79,61,19,64,30,57,39,37,71,72,41,56,44,18,2,76]
total_voltage = calculate_total_voltage(adapter_ratings, port_voltages)
print(total_voltage)  