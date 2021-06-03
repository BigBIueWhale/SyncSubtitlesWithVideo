timestampSub1 = float(input("\nEnter Timestamp 1 of subtitles (In Seconds): "))
timestampVid1 = float(input("\nEnter Timestamp 1 of actual video (In Seconds): "))
timestampSub2 = float(input("\nEnter Timestamp 2 of subtitles (In Seconds): "))
timestampVid2 = float(input("\nEnter Timestamp 1 of actual video (In Seconds): "))
R = (timestampVid1-timestampVid2)/(timestampSub1-timestampSub2)
d = timestampVid1-timestampSub1*R
print("\nJust multiply all timestamps in subtitle file by: " + str(R))
print("\nAnd then add to all timestamps: " + str(d))
input("")
