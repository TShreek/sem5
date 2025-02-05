library(readr)
library(ggplot2)

ipl_data <- read_csv("/Users/tshreek/Downloads/ipl_data.csv")
#print(head(ipl_data))
unique_teams<- unique(c(ipl_data$team1))
print(length(unique_teams))
print(unique_teams)
cat("Total Matches:", total_matches, "\n")
cat("Unique Teams:", length(unique_teams), "\n")
cat("Teams:", unique_teams, "\n")

# 📌 Task 3: Team Performance Analysis
team_wins <- arrange(
  summarize(
    group_by(ipl_data, Winner), 
    Matches_Won = n()
  ), 
  desc(Matches_Won)
)

avg_total_runs <- mean(ipl_data$Total.Runs, na.rm = TRUE)  
avg_total_wickets <- mean(ipl_data$Total.Wickets, na.rm = TRUE)

cat("Average Runs per Match:", avg_total_runs, "\n")
cat("Average Wickets per Match:", avg_total_wickets, "\n")

# 📌 Task 4: Venue Insights
most_frequent_venue <- slice(
  arrange(
    summarize(
      group_by(ipl_data, Venue), 
      Match_Count = n()
    ), 
    desc(Match_Count)
  ), 
  1
)

cat("Most Played Venue:", most_frequent_venue$Venue, "\n")

ggplot(team_wins, aes(x = reorder(Winner, -Matches_Won), y = Matches_Won, fill = Winner)) +
  geom_bar(stat = "identity") +
  ggtitle("Matches Won by Each Team") +
  xlab("Teams") +
  ylab("Matches Won") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1), legend.position = "none")
