from clinical_simulator import simulate_outbreak_dynamics

def render_ascii_dashboard():
    # Run historical simulations across changing seasonal rainfall vectors
    monsoon_months = ["June", "July", "August", "September"]
    rainfall_data = [150, 320, 410, 280] # Average regional metrics in mm
    
    print("=====================================================================")
    print("   DHAKA METROPOLITAN EPIDEMIOLOGICAL DATA DASHBOARD (MONSOON ACCELERATION)  ")
    print("=====================================================================")
    print(f"{'Month':<12} | {'Rainfall (mm)':<15} | {'Dengue Cases':<14} | {'AMR Mutation Risk'}")
    print("-" * 69)
    
    for month, rain in zip(monsoon_months, rainfall_data):
        metrics = simulate_outbreak_dynamics(rainfall_mm=rain, population=200000, self_medication_rate=65)
        print(f"{month:<12} | {rain:<15} | {metrics['predicted_dengue_cases']:<14} | {metrics['amr_acceleration_factor'] * 100:.1f}% Surge")
    print("=====================================================================")

if __name__ == "__main__":
    render_ascii_dashboard()