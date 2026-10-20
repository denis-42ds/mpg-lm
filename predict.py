import json
import sys
from pathlib import Path

coef = json.loads((Path(__file__).parent / "mpg_lm_coefficients.json").read_text())

def predict_hwy(displ: float) -> float:
    return coef["intercept"] + coef["slope_displ"] * displ

if __name__ == "__main__":
    displ = float(sys.argv[1]) if len(sys.argv) > 1 else 2.5
    print(f"displ={displ} L -> predicted hwy = {predict_hwy(displ):.1f} mpg")
