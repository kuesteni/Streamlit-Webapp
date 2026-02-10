import streamlit as st
import math

st.set_page_config(page_title="Wissenschaftlicher Taschenrechner", page_icon="🧮")
st.title("🧮 Wissenschaftlicher Taschenrechner (Abitur)")

# Session State für Rechenverlauf
if "verlauf" not in st.session_state:
    st.session_state.verlauf = []

# Auswahl der Operation
operation = st.selectbox(
    "Wähle eine Operation aus",
    [
        "Addition",
        "Subtraktion",
        "Multiplikation",
        "Division",
        "Potenzen",
        "Wurzel",
        "Prozentrechnung",
        "sin",
        "cos",
        "tan",
        "log"
    ]
)

# Dynamische Eingaben je nach Operation
if operation in ["Addition", "Subtraktion", "Multiplikation", "Division", "Potenzen", "Prozentrechnung"]:
    zahl1 = st.number_input("Zahl 1", value=0.0)
    zahl2 = st.number_input("Zahl 2", value=0.0)
else:
    zahl1 = st.number_input("Zahl", value=0.0)

# Berechnen-Button
if st.button("Berechnen"):
    try:
        # Grundrechenarten
        if operation == "Addition":
            ergebnis = zahl1 + zahl2
            rechnung = f"{zahl1} + {zahl2} = {ergebnis}"
        elif operation == "Subtraktion":
            ergebnis = zahl1 - zahl2
            rechnung = f"{zahl1} - {zahl2} = {ergebnis}"
        elif operation == "Multiplikation":
            ergebnis = zahl1 * zahl2
            rechnung = f"{zahl1} × {zahl2} = {ergebnis}"
        elif operation == "Division":
            if zahl2 == 0:
                raise ZeroDivisionError
            ergebnis = zahl1 / zahl2
            rechnung = f"{zahl1} ÷ {zahl2} = {ergebnis}"
        # Potenzen
        elif operation == "Potenzen":
            ergebnis = zahl1 ** zahl2
            rechnung = f"{zahl1} ^ {zahl2} = {ergebnis}"
        # Wurzeln
        elif operation == "Wurzel":
            if zahl1 < 0:
                raise ValueError("Wurzel aus negativer Zahl nicht erlaubt")
            ergebnis = math.sqrt(zahl1)
            rechnung = f"√{zahl1} = {ergebnis}"
        # Prozentrechnung
        elif operation == "Prozentrechnung":
            ergebnis = (zahl1 / 100) * zahl2
            rechnung = f"{zahl1}% von {zahl2} = {ergebnis}"
        # Trigonometrie in Grad
        elif operation == "sin":
            ergebnis = math.sin(math.radians(zahl1))
            rechnung = f"sin({zahl1}°) = {ergebnis}"
        elif operation == "cos":
            ergebnis = math.cos(math.radians(zahl1))
            rechnung = f"cos({zahl1}°) = {ergebnis}"
        elif operation == "tan":
            ergebnis = math.tan(math.radians(zahl1))
            rechnung = f"tan({zahl1}°) = {ergebnis}"
        # Logarithmus
        elif operation == "log":
            if zahl1 <= 0:
                raise ValueError("Logarithmus von 0 oder negativer Zahl nicht erlaubt")
            ergebnis = math.log10(zahl1)
            rechnung = f"log({zahl1}) = {ergebnis}"

        # Ergebnis anzeigen
        st.success(f"Ergebnis: {ergebnis}")
        # Rechenverlauf speichern
        st.session_state.verlauf.append(rechnung)

    except ZeroDivisionError:
        st.error("❌ Division durch 0 ist nicht erlaubt.")
    except ValueError as e:
        st.error(f"❌ Ungültige Eingabe: {e}")

# Rechenverlauf anzeigen
st.subheader("📜 Rechenverlauf")
if st.session_state.verlauf:
    for eintrag in reversed(st.session_state.verlauf):
        st.write(eintrag)
    if st.button("Verlauf löschen"):
        st.session_state.verlauf.clear()
else:
    st.write("Noch keine Berechnungen durchgeführt.")
