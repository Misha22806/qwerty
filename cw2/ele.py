class ElectricBox:
    def __init__(self, n_switches, n_outlets):
        self.n_switches = n_switches
        self.n_outlets = n_outlets
        self.switches = {}
        self.outlets = {}



    def install_switch(self, switch_number, switch_type):
                    if switch_number in self.switches:
                        print(f"Switch {switch_number} already installed.")
                    else:
                        self.switches[switch_number] = switch_type
                        print(f"Installed switch {switch_number} of type {switch_type}.")

    def uninstall_switch(self, switch_number):
        if switch_number in self.switches:
            del self.switches[switch_number]
            print(f"Uninstalled switch {switch_number}.")
        else:
            print(f"Switch {switch_number} not found.")

    def install_outlet(self, outlet_number, outlet_type):
        if outlet_number in self.outlets:
            print(f"Outlet {outlet_number} already installed.")
        else:
            self.outlets[outlet_number] = outlet_type
            print(f"Installed outlet {outlet_number} of type {outlet_type}.")

    def uninstall_outlet(self, outlet_number):
        if outlet_number in self.outlets:
            del self.outlets[outlet_number]
            print(f"Uninstalled outlet {outlet_number}.")
        else:
            print(f"Outlet {outlet_number} not found.")

        def __str__(self):
            return f"Electric box with {len(self.switches)} switches and {len(self.outlets)} outlets."
        
#Пример использования:


electric_box = ElectricBox(5, 3)
print(electric_box)  # Electric box with 0 switches and 0 outlets.

electric_box.install_switch(1, "Single pole")
electric_box.install_switch(2, "Double pole")
print(electric_box)  # Electric box with 2 switches and 0 outlets.

electric_box.install_outlet(1, "120V, 15A")
electric_box.install_outlet(2, "240V, 30A")
electric_box.install_outlet(3, "120V, 20A")
print(electric_box)  # Electric box with 2 switches and 3 outlets.

electric_box.uninstall_switch(2)
electric_box.uninstall_outlet(3)
print(electric_box)  # Electric box with 1 switches and 2 outlets.