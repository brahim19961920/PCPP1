#!/usr/bin/env python

from csv import DictReader, DictWriter
from os import chdir


def main():
    chdir("FilesProcessing")

    with open("exam_results.csv", newline="") as exams_csv_file:
        source_dict = DictReader(exams_csv_file, delimiter=",")
        new_dict = {}
        for element in source_dict:
            if new_dict.get(element["Exam Name"]) is None:
                new_dict[element["Exam Name"]] = {
                    "Candidates": [],
                    "Number of Passed Exams": 0,
                    "Number of Failed Exams": 0,
                    "Best Score": 0,
                    "Worst Score": 100,
                }

            if element["Candidate ID"] not in new_dict[element["Exam Name"]]["Candidates"]:
                new_dict[element["Exam Name"]]["Candidates"].append(element["Candidate ID"])

            if int(element["Score"]) > int(new_dict[element["Exam Name"]]["Best Score"]):
                new_dict[element["Exam Name"]]["Best Score"] = element["Score"]

            if int(element["Score"]) < int(new_dict[element["Exam Name"]]["Worst Score"]):
                new_dict[element["Exam Name"]]["Worst Score"] = element["Score"]

            if element["Grade"] == "Fail":
                new_dict[element["Exam Name"]]["Number of Failed Exams"] += 1
            else:
                new_dict[element["Exam Name"]]["Number of Passed Exams"] += 1

        with open("exams_report.csv", "w", newline="") as new_file:
            fields = [
                "Exam Name",
                "Number of Candidates",
                "Number of Passed Exams",
                "Number of Failed Exams",
                "Best Score",
                "Worst Score",
            ]
            dict_writer = DictWriter(new_file, delimiter=",", fieldnames=fields)
            dict_writer.writeheader()
            for exam in new_dict:
                dict_writer.writerow(
                    {
                        "Exam Name": exam,
                        "Number of Candidates": len(new_dict[exam]["Candidates"]),
                        "Number of Passed Exams": new_dict[exam]["Number of Passed Exams"],
                        "Number of Failed Exams": new_dict[exam]["Number of Failed Exams"],
                        "Best Score": new_dict[exam]["Best Score"],
                        "Worst Score": new_dict[exam]["Worst Score"],
                    }
                )


if __name__ == "__main__":
    main()
