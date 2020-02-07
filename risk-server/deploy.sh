gcloud builds submit --tag gcr.io/riskbot-267502/riskbot
gcloud beta run deploy --image gcr.io/riskbot-267502/riskbot
firebase deploy