## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

[The missing values or "NO DATA" entries in the data/phase0.txt dataset might be due to periods where the heart rate data was not recorded or where the sensor failed to capture accurate readings. It also may have occurred if the device was turned off or there was a data transmission error. By filtering out these values, we might risk losing important data, such as periods of inactivity or sensor errors, which could lead to incomplete analysis, bias, or limits of predictive analytics. Ignoring these values may also distort trustworthiness of the data and affect the accuracy of our analysis overall, especially in identifying sleep or exercise periods where missing data could represent important changes in heart rate.]

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

[Based on the visualizations on the graph in phase 0 png, sleep appears to occuring because it is the phase with the lowest maximum heart rate when compared to all other phases and it is constant for the longest period of time. From the data provided, the maximum heart rate during sleep is around 65 bpm, which is lower than the maximum heart rates of other phases, which are typically closer to 100 bpm. These findings on png 0 suggest that it is the phase with the lowest heart rate overall, confirming it as the sleep period.]

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

[From the data in phase 2 png it appears that exercise occurs in the because highest maximum heart rate is at 120 bpm. From the data, the maximum heart rate is higher than the maximum heart rates in other phases, which are typically below 100 bpm. This indicates that exercise is the phase with the highest heart rate.]

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

[This trend is appears to be observed in the awake activity phase 3 png. During awake periods, the average heart rate is relatively lower compared to exercise but higher than sleep, ao we can assume that the wake period is happening here. Additionally, the standard deviation is higher noticeably higher even visually on the graph, indicating more variation in heart rate during these periods, as people experience fluctuations in activity levels throughout the day.]
