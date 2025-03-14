# Streamlit Toolkit

This toolkit is tailor-made for my employer, providing a comprehensive set of tools for various data processing tasks using Streamlit. Streamlit is a popular open-source framework for building data apps quickly and easily with Python.

- Customize your Streamlit app appearance by modifying the config.toml file located in the .streamlit directory.
- Ensure you have set up the necessary configurations, including the randomly chosen password stored in secrets.toml within the .streamlit directory.

Run the Streamlit app using the following command:
```
streamlit run Accueil.py
```

# Note

The most interesting aspects of this toolkit lie within the following pages:

- 5extract_commande.py: This page contains functionality for extracting information from unstructured text files containing commands and organizing them into an Excel file for better analysis.
- 6pdf_excel.py: Here, you'll find tools for converting PDF files to Excel format.
- 8match.py: This page provides matching functionalities with difflib.
  
Additionally, explore the classes and functions associated with these pages within the func package.

# Future Improvements

Pages such as ean_gen are functional, but there is substantial refactoring required to transition from script-based implementation to object-oriented programming (OOP) for better organization and maintainability.

