import random
from datetime import date

# create programm that supports a library of movies and series
print("Library of Movies and Series")

# create Video base class
class Video:
    def __init__(self, title, release_date, genre, num_plays):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.num_plays = num_plays

    def play(self):
        """method increasing the num_plays for a video, inherited by Movie and Series class"""
        self.num_plays += 1

    def  __str__(self):
        """string representation of the Video object"""
        return f"{self.title} {self.release_date}"
    
# create Movie class that inherits from Video class
class Movie(Video):
    def __init__(self, title, release_date, genre, num_plays):
        super().__init__(title, release_date, genre, num_plays)

# create Series class that inherits from Video class and adds episode and season number attributes
class Series(Video):
    def __init__(self, title, release_date, genre, num_plays, episode_num, season_num):
        super().__init__(title, release_date, genre, num_plays)
        self.episode_num = episode_num
        self.season_num = season_num
    
    def __str__(self):
        """
        string representation of the Series object
        with the season and episode number in two notation format
        """
        return f"{self.title} S{self.season_num:02d}E{self.episode_num:02d}"
    
# create Library class with an empty list to store videos
class Library:
    def __init__(self):
        self.library = []

    def add_video(self, video):
        """create the method to add a video to the library"""
        self.library.append(video)

    def get_movies(self):
        """create the function to get movies only from the library and sorted them alpabetically"""
        movies = [video for video in self.library if isinstance(video, Movie)]
        return sorted(movies, key=lambda x: x.title)
    
    def get_series(self):
        """create the function to get series only from the library and sorted them alpabetically"""
        series = [video for video in self.library if isinstance(video, Series)]
        return sorted(series, key=lambda x: x.title)
    
    def search(self, title):
        """method to search for a video by its title"""
        result = []
        for video in self.library:
            if title.lower() in video.title.lower():
                result.append(video)
        return result
    
    def generate_views(self):
        """method to generate random views for a random video in the library"""
        video = random.choice(self.library)
        views = random.randint(1, 100)
        for _ in range(views):
            video.play()

    def generate_views_multiple_times(self, num_times):
        """method to generate views multiple times"""
        for _ in range(num_times):
            self.generate_views()

    def top_titles(self, num_titles, content_type):
        """method to get the top titles based on the number of plays"""
        if content_type =='movies':
            sorted_videos = sorted(self.library, key=lambda x: x.num_plays, reverse=True)
            top_titles = [video for video in sorted_videos if isinstance(video, Movie)]
        elif content_type == 'series':
            sorted_videos = sorted(self.library, key=lambda x: x.num_plays, reverse=True)
            top_titles = [video for video in sorted_videos if isinstance(video, Series)]
        else:
            top_titles = []
        return top_titles[:num_titles]
    
    def add_full_season(self, title, release_date, genre, season_num, episode_num):
        """method to add a full season of a series to the library"""
        for episode_num in range(1, num_episodes + 1):
            series = Series(title, release_date, genre, 0, episode_num, season_num)
            self.add_video(series)
    
    @staticmethod
    def get_episode_count(series):
        """static method to get the number of episodes available in a series in the library"""
        episodes = [video for video in series.library if isinstance(video, Series)]
        return len((episodes))
    

# create the main programm
def main():
    library = Library()

    # create Movie objects
    movie1 = Movie("Pulp Fiction", 1994, "Crime", 0)
    movie2 = Movie("Django", 2012, "Western", 0)
    movie3 = Movie("Inglourious Basterds", 2009, "War", 0)

    # add movies to the library
    library.add_video(movie1)
    library.add_video(movie2)
    library.add_video(movie3)

    # create Series object
    series1 = Series("Game of Thrones", 2011, "Fantasy", 0,1,1)
    series2 = Series("The Wolking Dead", 2010, "Horror", 0,1,1)
    series3 = Series("Braking Bad", 2008, "Drama",0,1,1)

    # add series to the library
    library.add_video(series1)
    library.add_video(series2)
    library.add_video(series3)

    #generate views for the videos in the library
    library.generate_views_multiple_times(10)

    # get the current date
    today = date.today().strftime("%d.%m.%Y")

    # display the most popular movies and series
    print(f"Most popular movies and series on {today}:")
    top_titles = library.top_titles(3, 'movies') + library.top_titles(3, 'series')
    for i, title in enumerate(top_titles, 1):
        print(f"{i}, {title}")

if __name__ == '__main__':
    main()