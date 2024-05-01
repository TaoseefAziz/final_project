"""
LaunchAnnounced
Launch_Status
Body_Dimensions
Body_Weight
Body_SIM
Display_Type
Display_Size
Display_Resolution
Platform_OS
Platform_Chipset
Platform_CPU
Memory_Card slot
Memory_Internal
Main Camera_Single
Main Camera_Video 
Selfie camera_Single
Selfie camera_Video
"""
import convert_launch_announced_and_launch_status
import convert_body_dimensions
import convert_body_weight
import convert_body_sim
import convert_display_type
import convert_display_size
import convert_display_resolution
import convert_platform_os
import convert_platform_chipset
import convert_platform_cpu
import convert_memory_card_slot
import convert_memory_internal
import convert_main_camera_single
import convert_battery_type
import pandas as pd
pd.options.mode.chained_assignment = None

SOURCE_FILE = "specifications.csv"
OUTPUT_FILENAME = "converted_all_taoseef.csv"

def main():
    specs_df = pd.read_csv(SOURCE_FILE)
    print(specs_df.shape)
    out_df = convert_launch_announced_and_launch_status.convert_launch_announced_and_launch_status(specs_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_battery_type.convert_battery_type(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_body_dimensions.convert_body_dimensions(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_body_weight.convert_body_weight(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_body_sim.convert_body_sim(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_display_type.convert_display_type(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_display_size.convert_display_size(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_display_resolution.convert_display_resolution(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_platform_os.convert_platform_os(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_platform_chipset.convert_platform_chipset(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_platform_cpu.convert_platform_cpu(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_memory_card_slot.convert_memory_card_slot(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_memory_internal.convert_memory_internal(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)

    out_df = convert_main_camera_single.convert_main_camera_single(out_df)
    out_df.to_csv(OUTPUT_FILENAME, index = False)
    
    out_df.to_csv(OUTPUT_FILENAME, index = False)

main()