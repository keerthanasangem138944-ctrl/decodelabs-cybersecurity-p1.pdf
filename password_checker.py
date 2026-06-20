# =========================================================
# DECODELABS: CYBERSECURITY PROJECT 1
# PROJECT: PASSWORD STRENGTH CHECKER
# TIME COMPLEXITY REQUIREMENT: O(n) USING ANY()
# =========================================================

def check_password_strength(password):
    # STEP 1: Length Boundary (The Zero Point Check)
    if len(password) < 8:
        return "Weak (Reason: Too short, must be at least 8 characters)"
    
    # STEP 2: Pattern Recognition using short-circuit any()
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)
    
    # STEP 3: Risk Classification (Counting metrics)
    # We count how many conditions are met
    conditions_met = sum([has_upper, has_digit, has_symbol])
    
    if conditions_met == 3:
        return "Strong"
    elif conditions_met == 2:
        return "Medium"
    else:
        return "Weak"

# --- INPUT / OUTPUT HANDLING ---
if __name__ == "__main__":
    print("--- DecodeLabs Password Security System Active ---")
    user_password = input("Enter a password to evaluate: ")
    
    # Process and Output result
    result = check_password_strength(user_password)
    print(f"Password Evaluation Security Risk Result: {result}")