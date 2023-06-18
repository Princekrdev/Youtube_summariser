import streamlit as st
from main import summarize_youtube_video


def main():
    st.title("YouTube Video Summary")

    # Get the YouTube link from the user
    youtube_link = st.text_input("Enter the YouTube video link")

    # Summarize the YouTube video on button click
    if st.button("Summarize"):
        if youtube_link:
            # Call your summarization function from app.py
            summary = summarize_youtube_video(youtube_link)

            # Display the summary1 in a styled box
            st.success("Summary :")
            st.info(summary)

        else:
            st.warning("Please enter a YouTube video link.")


if __name__ == "__main__":
    main()

