import json

# Setup: Create initial config.json file
initial_config = {"name": "Adeleke", "theme": "dark"}
with open("config.json", "w") as file:
    json.dump(initial_config, file, indent=4)

# 1. Read the config
with open("config.json", "r") as file:
    config = json.load(file)

# 2. Print each setting
print("Current Configurations:")
for key, value in config.items():
    print(f"{key}: {value}")

# 3. Ask user if they want to update a value
update_key = input("\nEnter the setting name you want to update (or press Enter to skip): ").strip()

if update_key in config:
    new_value = input(f"Enter new value for {update_key}: ")
    config[update_key] = new_value
    
    # 4. Save updated config back to file
    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)
    print("Config updated successfully.")
elif update_key:
    print("Setting not found.")
