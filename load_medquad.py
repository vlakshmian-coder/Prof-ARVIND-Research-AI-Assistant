# ==========================================================
# Project: Medical Q&A Chatbot
# File: load_medquad.py
# Author: Vijayalakshmi Narayanan
# Description:
# Loads all MedQuAD XML files and extracts
# Question-Answer pairs.
# ==========================================================

import os
import xml.etree.ElementTree as ET


def load_medquad():

    current_dir = os.path.dirname(os.path.abspath(__file__))

    dataset_path = os.path.join(
        current_dir,
        "..",
        "data",
        "MedQuAD-master"
    )

    medical_data = []

    print("\nLoading MedQuAD Dataset...\n")

    for folder in os.listdir(dataset_path):

        folder_path = os.path.join(dataset_path, folder)

        if not os.path.isdir(folder_path):
            continue

        print(f"Reading Folder: {folder}")

        for file in os.listdir(folder_path):

            if not file.endswith(".xml"):
                continue

            xml_file = os.path.join(folder_path, file)

            try:

                tree = ET.parse(xml_file)
                root = tree.getroot()

                qa_pairs = root.find("QAPairs")

                if qa_pairs is None:
                    continue

                for qa in qa_pairs.findall("QAPair"):

                    question = qa.findtext("Question")
                    answer = qa.findtext("Answer")

                    if question and answer:

                        medical_data.append(
                            {
                                "question": question.strip(),
                                "answer": answer.strip(),
                                "source": folder
                            }
                        )

            except Exception as error:
                print(f"Error reading {file}: {error}")

    print("\n===================================")
    print(f"Total Q&A pairs loaded: {len(medical_data)}")
    print("===================================\n")

    return medical_data


if __name__ == "__main__":

    data = load_medquad()

    print("\nFirst 5 Question-Answer Pairs:\n")

    for item in data[:5]:

        print("Source :", item["source"])
        print("Question:", item["question"])
        print("Answer:", item["answer"][:120], "...")
        print("-" * 70)