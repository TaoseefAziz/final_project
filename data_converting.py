SPECIFICATIONS_FILE = "sepcifications.csv"

columns_to_convert = ["Launch_Announced",    "Launch_Status",    "Body_Dimensions",
    "Body_Weight",    "Body_SIM",    "Body_",    "Display_Type",    "Display_Size",    "Display_Resolution",
    "Platform_OS",    "Platform_Chipset",    "Platform_CPU",    "Memory_Card slot",    "Memory_Internal",
    "Main Camera_Single",    "Main Camera_Video",    "Selfie camera_Single",    "Selfie camera_Video",
    "Sound_Loudspeaker",    "Sound_3.5mm jack",     "Comms_WLAN",    "Comms_Bluetooth",
    "Comms_Positioning",    "Comms_NFC",    "Comms_Radio",    "Comms_USB",    "Features_Sensors",
    "Battery_Type",    "Battery_Talk time",    "Misc_Colors",    "Misc_Price",    "Network_3G bands",
    "Network_4G bands",    "Network_",    "Network_Speed",    "Platform_GPU"]

print("Taoseef")
print("_______________________________________\n")
for i in range(int(len(columns_to_convert)/2)):
    print(columns_to_convert[i])
print()


print("Bryan")
print("_______________________________________\n")
for i in range(int(len(columns_to_convert)/2), len(columns_to_convert)):
    print(columns_to_convert[i])
print()
