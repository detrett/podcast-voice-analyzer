# Podcast Voice and Recording Analyzer

## Option
Option B: Podcast Voice and Recording Analysis

## Student
Name: ALAN BLANCO ALQUÉZAR
Student number: 354528

## Description

This project is a small Python application for analyzing acoustic observations from a podcast recording.

The application represents a speaker's usual acoustic profile and compares it with observations collected from a recording session.
It calculates average acoustic measurements, checks the quality of the recording, and classifies the speaker's delivery.

The application also handles observations where speech is missing and validates measurements before they are included in the analysis.


## Class Design

For the four mandatory classes requested in the assignment, we have:

### SpeakerProfile

`SpeakerProfile` stores the acoustic values that are considered usual for a particular speaker. These values are used as a baseline when
comparing a recording with the speaker's normal speaking style.

### Observation

`Observation` represents one observation window from a recording. It stores whether speech was detected together with pitch, energy,
speech rate, pause ratio, background noise, and signal quality.

This class also validates the observation data when an object is created.

### RecordingSession

`RecordingSession` represents one complete recording session. It contains a `SpeakerProfile` and a list of `Observation` objects.
The observations are stored in a private `_observations` attribute and accessed through the `observations` property.

### Analyzer

`Analyzer` performs the calculations and classification for a recording session. It calculates average acoustic measurements,
compares them with the speaker's usual profile, evaluates recording quality, and produces the final structured analysis result.


## Object-Oriented Design

### Composition

Composition is used in `RecordingSession`.

A recording session contains a `SpeakerProfile` and multiple `Observation` objects. These objects represent parts of the session
rather than being types of the session itself.

This also allows the same classes to be reused independently.

### Encapsulation

An example of encapsulation can be found in `RecordingSession`, which stores its observations in the private `_observations` attribute.

A property named `observations` provides controlled access to the list.

### Inheritance and Overriding

Inheritance is not used in this project because there is no natural "is-a" relationship between the main concepts.

For example, an `Observation` is not a type of `RecordingSession`, and an `Analyzer` is not a type of `SpeakerProfile`.

Using inheritance just to satisfy the requirement would make the design less meaningful, so instead composition was favoured for the design of this app.

### Static Method

`Analyzer.is_within_tolerance()` is a static method because it does not need information from a particular analyzer or recording
session.

It just checks whether a value is within a given tolerance.

## Analysis Rules

The application uses the following rules (chosen arbitrarily but trying to follow logic):

- At least 50% of the observation windows must contain usable speech for the recording to have sufficient data.
- Background noise above 0.70 is classified as high.
- Signal quality below 0.50 is considered poor.
- Pitch uses a tolerance of 10.
- Energy uses a tolerance of 0.05.
- Speech rate uses a tolerance of 10.
- Pause ratio uses a tolerance of 0.05.
- An increase in energy above the energy tolerance results in an `energetic` classification.
- A lower speech rate together with a higher pause ratio results in a `deliberate` classification.
- If all main measurements are within their normal values, the delivery is classified as `consistent`.
- Other usable recordings that don't meet these requirements are instead classified as `temporarily varied`.
- High background noise takes priority and results in a `noise affected` classification.
- Recordings without enough usable speech are classified as `insufficient data`.

## Validation

The `Observation` class checks for missing and impossible values.

For observations where speech is present, pitch, energy, speech rate, and pause ratio must be provided.

The numeric values are also checked against their expected ranges.
For example, energy, pause ratio, background noise, and signal quality must be between 0 and 1.

Invalid generated observations are excluded from the recording rather than stopping the entire analysis.

## Project Structure

- `main.py` - runs the application and analyzes the available scenarios
- `speaker.py` - contains the `SpeakerProfile` class
- `observation.py` - contains the `Observation` class
- `recording_session.py` - contains the `RecordingSession` class
- `analyzer.py` - contains the `Analyzer` class
- `sample_data.py` - converts the supplied sample data into application objects
- `report.py` - prints the analysis results
- `utils.py` - contains reusable calculation and formatting functions
- `data_generator.py` - supplied starter data generator
- `tests.py` - automated tests
- `requirements.txt` - project dependencies

## Installation

This project uses only the Python standard library, so no external packages need to be installed.

Clone the repository and open a terminal in the project root.

Run the application with:

    python main.py

Run the tests with:

    python -m unittest tests.py

## Example Output

A typical analysis produces output similar to:

    Scenario: consistent

    === Podcast Recording Analysis ===
    Speaker: SP001
    Usable speech windows: 12

    Delivery classification: consistent
    Recording quality: good

The application also displays the calculated acoustic measurements and their differences from the speaker's usual profile.

## Test Scenarios

The application includes five scenarios supplied by the starter data generator:

- `consistent`
- `energetic`
- `deliberate`
- `noise_affected`
- `insufficient_data`

These cover normal speaking behavior as well as different unusual and poor-quality recording conditions.

## Known Limitations

The application works with generated sample data rather than recording or processing real audio.

The classification thresholds are manually defined for the project, so the classifications should not be interpreted as professional
speech or audio analysis.

The application also excludes invalid observations rather than attempting to repair their values.

No external libraries, databases, graphical interfaces, or external APIs are used.