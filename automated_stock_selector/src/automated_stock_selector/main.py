#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from automated_stock_selector.crew import AutomatedStockSelector

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    sector=input("Enter the sector: ")
    inputs = {
        'sector': sector,
    }
    
    result=AutomatedStockSelector().crew().kickoff(inputs=inputs)
    print("\n\n=== FINAL DECISION ===\n\n")
    print(result)
    
if __name__ == "__main__":
    run()
