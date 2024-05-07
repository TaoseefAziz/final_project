import pandas as pd

SOURCE_FILE = "converted_all_taoseef_extended_truncated.csv"
OUTPUT_FILENAME = "converted_all_taoseef_extended_dropped.csv"

def main():
    specs_df = pd.read_csv(SOURCE_FILE)
    specs_df = specs_df.dropna(subset=["Launch_year","IsAvailable","Battery_Capacity","Battery_Removability","Body_length_mm","Body_width_mm","Body_depth_mm",
    "Body_Weight_g","num_slots_sim","has_mini_sim","has_nano_sim","has_micro_sim","has_e_sim","stand-by_sim","hybrid_sim","platform_cpu_count","platform_cpu_speed_ghz",
    "display_tech","display_refresh","display_diagonal_inches","display_area_cm2","display_screen_body_ratio","main_camera_single_mp",
    "display_width_px","display_height_px","display_density","platform_os","platform_chipset_manufacturer","memory_card_slot","memory_internal_storage","memory_ram"],axis=0) 
    specs_df.to_csv(OUTPUT_FILENAME, index = False)
main()