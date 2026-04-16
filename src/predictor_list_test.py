predictor_columns = [
    # OAI ActiGraph summary
    "V06AACNT",               # Total activity count
    "V06AALTMNT",             # Light activity minutes
    "V06AAMDMNT",             # Moderate activity minutes
    "V06AAMVMNT",             # Moderate-to-vigorous activity minutes
    "V06AAVMNT",              # Vigorous activity minutes
    "V06AAMVBMT",             # MVPA bout minutes
    "V06AAVBMT",              # Vigorous bout minutes
    "V06ANVDAYS",             # Number of valid wear days
    "V06AACSM03",             # ACSM guideline compliance ratio

    # Derived sleep metrics (accelerometry-based)
    "V06CESD11",
    "wake_minute_mean",
    "wake_minute_sd",
    "sleep_minute_mean",
    "sleep_minute_sd",
    "wear_duration_mean",
    "valid_days",
    "weekly_guideline_gap_minutes",

    # Bout structure: sedentary
    "mean_sedentary_bout_count",
    "mean_sedentary_bout_mean_duration",
    "mean_sedentary_bout_max_duration",
    "mean_sedentary_bout_total_minutes",

    # Bout structure: light
    "mean_light_bout_count",
    "mean_light_bout_mean_duration",
    "mean_light_bout_max_duration",
    "mean_light_bout_total_minutes",

    # Bout structure: moderate
    "mean_moderate_bout_count",
    "mean_moderate_bout_mean_duration",
    "mean_moderate_bout_max_duration",
    "mean_moderate_bout_total_minutes",

    # Bout structure: vigorous
    "mean_vigorous_bout_count",
    "mean_vigorous_bout_mean_duration",
    "mean_vigorous_bout_max_duration",
    "mean_vigorous_bout_total_minutes",

    # Bout structure: MVPA
    "mean_mvpa_bout_count",
    "mean_mvpa_bout_mean_duration",
    "mean_mvpa_bout_max_duration",
    "mean_mvpa_bout_total_minutes",

    # Bout structure: active (all non-sedentary)
    "mean_active_bout_count",
    "mean_active_bout_mean_duration",
    "mean_active_bout_max_duration",
    "mean_active_bout_total_minutes",
]