import sys, socket
from tello_sim_text import Simulator

ADDRESS = '0.0.0.0'
PORT = 18889

drone = None
supported_commands = ["takeoff", "land", "up", "down", "right", "left", "forward", "back", "cw", "ccw", "flip"]

def main() -> int:
    print("                                       ")   
    print(" ______    ____       ______        __ ")
    print("/_  __/__ / / /__    /_  __/____ __/ /_")
    print(" / / / -_) / / _ \    / / / -_) \ / __/")
    print("/_/  \__/_/_/\___/   /_/  \__/_\_\\__/ ")
    print("                                       ")
    print("    A text-based DJI Tello Emulator    ")
    print("                                       ")                                       
    print("Connecting...")
    is_running = True
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((ADDRESS, PORT))
    
    print("Emulator listening on {}:{}".format(ADDRESS, PORT))
    while(is_running):
        try:
            msg, client_address = server_socket.recvfrom(1024)
            data = msg.decode('utf-8').rstrip()
            if data.lower() == 'halt':
                print("Halt command received. Shutting down emulator...")
                is_running = False
            else:
                res = process_command(data)
                reply(server_socket, client_address, res)
        except Exception as ex:
            print(ex)

    server_socket.close()
    print("Emulator successfully stopped. Bye!")

def process_command(data):
    global drone
    tokens = data.lower().split(" ")
    command = tokens[0]
    if command == "command":
        drone = Simulator()
    elif command in supported_commands:
        try:
            if not drone:
                return "Error"
            elif len(tokens) == 1:
                getattr(drone, command)()
            else:
                arg = tokens[1] if not tokens[1].isdigit() else int(tokens[1])
                getattr(drone, command)(arg)
        except Exception as ex:
            print(ex)
            return "Error"
    else:
        print("Command '{}' not yet supported".format(data))
    return "OK"
    

def reply(server_socket, client_address, res):
    payload = res.encode('utf-8')
    server_socket.sendto(payload, client_address)
    

if __name__ == "__main__":
    sys.exit(main())