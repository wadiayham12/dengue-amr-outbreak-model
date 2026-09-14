import math

def simulate_outbreak_dynamics(rainfall_mm, population, self_medication_rate):
    """
    Simulates localized viral transmission vectors and resulting bacterial selection curves.
    """
    # Estimate Dengue transmission surge based on rainfall volume
    dengue_cases = int(rainfall_mm * 4.5 * (population / 100000))
    
    # Model secondary risk: population self-medicating with antibiotics during viral fever
    empirical_misuse_events = int(dengue_cases * (self_medication_rate / 100))
    
    # Statistical modeling of selective pressure accelerating AMR mutations
    amr_selection_coefficient = math.log10(empirical_misuse_events + 1) * 0.15
    
    return {
        "predicted_dengue_cases": dengue_cases,
        "misuse_events": empirical_misuse_events,
        "amr_acceleration_factor": round(amr_selection_coefficient, 4)
    }

if __name__ == "__main__":
    # Test simulation for Dhaka during peak monsoon conditions
    dhaka_test = simulate_outbreak_dynamics(rainfall_mm=350, population=500000, self_medication_rate=72)
    print("--- Dhaka Epidemiological Simulation Metrics ---")
    for metric, value in dhaka_test.items():
        print(f"{metric.replace('_', ' ').title()}: {value}")