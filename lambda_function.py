from google.ads.googleads.client import GoogleAdsClient 

def lambda_handler(): 
    GoogleAdsClient.load_from_storage()
