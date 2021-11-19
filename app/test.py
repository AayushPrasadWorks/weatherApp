from datetime import datetime, timezone
import getWeather

def main():
    location = input("Enter location:")
    now = datetime.utcnow()
    
    res = getWeather.getSevenDay(location, 'd4450502dc2d565c203526c49b66b8cc')
    print(res)

if __name__ == "__main__":
    main()