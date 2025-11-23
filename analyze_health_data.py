#!/usr/bin/env python3
"""
Health Sensor Data Analysis Script

Complete the TODO sections to analyze health sensor data using NumPy.
This script demonstrates basic NumPy operations for data loading, statistics,
filtering, and report generation.
"""

import numpy as np


def load_data(filename):
    """Load CSV data using NumPy.
    
    Args:
        filename: Path to CSV file
        
    Returns:
        NumPy structured array with all columns
    """
     # This code is provided (np.genfromtxt not covered in lecture)
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'),
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]
    
    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data

def calculate_statistics(data):
    """Calculate basic statistics for numeric columns.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with statistics
    """
    # TODO: Calculate average heart rate using data['heart_rate'].mean()
    avg_heart_rate = data['heart_rate'].mean()
    print(f"Mean heart rate: {avg_heart_rate:.2f}")
    # TODO: Calculate average systolic BP using data['blood_pressure_systolic'].mean()
    avg_systolic_bp = data['blood_pressure_systolic'].mean()
    print(f"Mean systolic BP: {avg_systolic_bp:.2f}")
    # TODO: Calculate average glucose level using data['glucose_level'].mean()
    avg_glucose = data['glucose_level'].mean()
    print(f"Mean glucose level: {avg_glucose:.2f}")
    # TODO: Return as dictionary with keys: 'avg_heart_rate', 'avg_systolic_bp', 'avg_glucose'
    return {'avg_heart_rate': avg_heart_rate, 'avg_systolic_bp': avg_systolic_bp, 'avg_glucose': avg_glucose}


def find_abnormal_readings(data):
    """Find readings with abnormal values.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with counts
    """
    # TODO: Count readings where heart rate > 90 using boolean indexing
    # Example: high_hr_count = len(data[data['heart_rate'] > 90])
    # Or: high_hr_count = (data['heart_rate'] > 90).sum()
    heart_rate_mask = data['heart_rate'] > 90
    high_hr_count = heart_rate_mask.sum()
    # TODO: Count readings where systolic BP > 130 using boolean indexing
    # Example: high_bp_count = len(data[data['blood_pressure_systolic'] > 130])
    high_bp_count = (data['blood_pressure_systolic'] > 130).sum()
    # TODO: Count readings where glucose > 110 using boolean indexing
    # Example: high_glucose_count = len(data[data['glucose_level'] > 110])
    high_glucose_count = (data['glucose_level'] > 110).sum()
    # TODO: Return dictionary with keys: 'high_heart_rate', 'high_blood_pressure', 'high_glucose'
    return {'high_heart_rate': high_hr_count, 'high_blood_pressure': high_bp_count, 'high_glucose': high_glucose_count}


def generate_report(stats, abnormal, total_readings):
    """Generate formatted analysis report.
    
    Args:
        stats: Dictionary of statistics
        abnormal: Dictionary of abnormal counts
        total_readings: Total number of readings
        
    Returns:
        Formatted string report
    """
    # Use the provided values (do not re-compute from an empty local variable).
    avg_heart_rate = stats.get('avg_heart_rate', 0.0)
    avg_systolic_bp = stats.get('avg_systolic_bp', 0.0)
    avg_glucose = stats.get('avg_glucose', 0.0)
    high_hr_count = abnormal.get('high_heart_rate', 0)
    high_bp_count = abnormal.get('high_blood_pressure', 0)
    high_glucose_count = abnormal.get('high_glucose', 0)
    all_averages = (avg_heart_rate, avg_systolic_bp, avg_glucose)
    all_abnormals = (high_hr_count, high_bp_count, high_glucose_count)
    #Converting the Numpy scalars to integers - copilot helped me breakdown the syntax and figure this one out since I couldn't find anything in the lecture to help me solve this problem
    all_averages = tuple(x.item() for x in all_averages)
    all_abnormals = tuple(x.item() for x in all_abnormals)

    report = (
        f"Health Data Analysis Report\n"
        f"---------------------------\n\n"
        f"Heart Rate (avg): {avg_heart_rate:.1f} bpm\n"
        f"Systolic BP (avg): {avg_systolic_bp:.1f} mmHg\n"
        f"Glucose Level (avg): {avg_glucose:.1f} mg/dL\n\n"
        f"High Heart Rate Readings (>90 bpm): {high_hr_count}\n"
        f"High Systolic BP Readings (>130 mmHg): {high_bp_count}\n"
        f"High Glucose Readings (>110 mg/dL): {high_glucose_count}\n\n"
        f"Total Readings: {total_readings}\n\n"
        f"All Averages: {all_averages}\n"
        f"All Abnormal Counts: {all_abnormals}\n"
    )
    return report

def save_report(report, filename):
    """Save report to file.
    
    Args:
        report: Report string
        filename: Output filename
    """
    # TODO: Write the report to a file using open() with 'w' mode
    # Example: with open(filename, 'w') as f:
    #              f.write(report)
    with open(filename, 'w') as f:
        f.write(report)
    return None

def main():
    """Main execution function."""
    # TODO: Load the data from 'health_data.csv' using load_data()
    data = load_data('health_data.csv')
    # TODO: Calculate statistics using calculate_statistics()
    # TODO: Find abnormal readings using find_abnormal_readings()
    # TODO: Calculate total readings using len(data)
    # TODO: Generate report using generate_report()
    stats = calculate_statistics(data)
    abnormal = find_abnormal_readings(data)
    total_readings = len(data)
    report = generate_report(stats, abnormal, total_readings)
    # TODO: Save to 'output/analysis_report.txt' using save_report()
    save_report(report, 'output/analysis_report.txt')
    # TODO: Print success message
    print("Analysis report generated and saved successfully.")
    # Do not recurse; finish after one run.
    return None

if __name__ == "__main__":
    main()