import sys  
import time  
import subprocess
import re  # regex import

def regulate_temperature(min_threshold, max_threshold, temperatures):
    try:
        in_house_temperature = None  
        start_time = time.time()

        for external_temp in temperatures:
            # Stop  printing after 48 secondes
            if time.time() - start_time > 48:
                break

            # Init temp inside
            if in_house_temperature is None:
                in_house_temperature = float(external_temp)

            external_temp = float(external_temp)
            action = "nothing"

            # Ajust heat and cooling depends on threshold 
            if in_house_temperature < min_threshold:
                action = "heating"
                in_house_temperature += 0.5  
            elif in_house_temperature > max_threshold:
                action = "cooling"
                in_house_temperature -= 0.5  
            else:
                # Move to external temperature  
                if in_house_temperature < external_temp:
                    in_house_temperature += 0.25  
                elif in_house_temperature > external_temp:
                    in_house_temperature -= 0.25

            # Status external temp  
            print(f"External temperature: {external_temp:.2f} | Action: {action} | In-house temperature: {in_house_temperature:.2f}")

    except ValueError:
        print("Invalid temperature input.")
        return

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python expert_system.py <min_threshold> <max_threshold>")
    else:
        try:
            min_threshold = float(sys.argv[1])
            max_threshold = float(sys.argv[2])
            result = subprocess.run(['python3', './environment.py', 'spring'], capture_output=True, text=True)
            
            # regex to extract temperature 
            temperatures = re.findall(r"(\d+\.?\d*)", result.stdout)  # Decimal extract  
            temperatures = list(map(float, temperatures))  # float converting

            regulate_temperature(min_threshold, max_threshold, temperatures)  # capture temperature 
        except ValueError:
            print("Thresholds must be numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")