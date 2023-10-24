import requests
from multiprocessing import Pool

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdgSLozEfmb5gKE8d_hyXBVRiXpvuFFUXdTVlPOVuRLfDxySg/formResponse"
MULTI_CHOICE_ENTRY_ID = "entry.953604185"

def submit_vote(choice_id):
    data = {
        MULTI_CHOICE_ENTRY_ID: choice_id
    }

    response = requests.post(FORM_URL, data=data)
    if response.status_code == 200:
        print(f"Successfully voted for choice {choice_id}!")
    else:
        print(f"Failed to vote for choice {choice_id}.")

def main():
    CHOICE_ID_FOR_YOUR_NAME = "Twyford, Declan"
    num_votes = 100000000  # You can change this to the number of votes you want to submit

    # Create a pool of worker processes
    with Pool() as pool:
        # Use the pool to submit votes concurrently
        pool.map(submit_vote, [CHOICE_ID_FOR_YOUR_NAME] * num_votes)

if __name__ == "__main__":
    main()
