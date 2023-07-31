<!DOCTYPE html>
<html>

<head>
  <h1> • Recommendation Systems by Word Vecorization </h1>
  
</head>

<body>

  <table>
    <tr>
      <td>
        <img src="https://img.freepik.com/free-vector/team-analysts-working-brand-reputation-social-media_74855-20739.jpg?w=826&t=st=1690830755~exp=1690831355~hmac=424f52da3b7653be2d576a8c58f159397aa0855a6b8e61eb7dda9c22f709b5dd" alt="Project Logo" width="1000">
      </td>
      <!-- Project name and description on the right -->
      <td>
        <h1>  🎬 🍿 Movie and Book Recommendation Systems using Streamlit 📚📖</h1>
        <p>Welcome to our groundbreaking project that combines the power of cutting-edge machine learning techniques to offer personalized movie and book recommendations tailored to individual preferences. Whether you're a movie enthusiast or an avid reader, our system aims to cater to your unique interests and provide delightful entertainment experiences!</p>
      </td>
    </tr>
  </table>

  <!-- ... (rest of the README content) -->

</body>

  <h2>Description 🎯</h2> 
  <p>Welcome to our Movie and Book Recommendation System! 🌟 In this groundbreaking project, we present a comprehensive platform that combines the power of cutting-edge machine learning techniques to offer personalized movie and book recommendations tailored to individual preferences. Whether you're a movie enthusiast or an avid reader, our system aims to cater to your unique interests and provide delightful entertainment experiences! 🎬📚🍿📖</p>

  <h2>Dependencies 📚</h2>
  <p>Ensure you have the following dependencies installed on your system before running the recommendation apps:</p>
  <ul>
    <li>Streamlit</li>
    <li>Pandas</li>
    <li>NumPy</li>
    <li>Scikit-learn</li>
  </ul>
  <p>You can quickly set up the required environment by using the following command:</p>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h2>Using Kaggle Datasets 📊</h2>
  <p>We are excited to leverage the rich and diverse datasets provided by Kaggle to power our Movie and Book Recommendation System! 🎉</p>

  <h3>Movie Dataset:</h3>
  <p>Kaggle Dataset Link: <a href="https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv">TMDB Movie Metadata</a></p>
  <p>Description: This dataset contains valuable metadata for over 5000 movies, including details such as movie title, genres, runtime, revenue, budget, and more. Our Movie Recommendation System utilizes this dataset to offer personalized movie suggestions based on user preferences.</p>

  <h3>Book Dataset:</h3>
  <p>Kaggle Dataset Link: <a href="https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset">Book Recommendation Dataset</a></p>
  <p>Description: With a vast collection of books and their ratings, this dataset enables our Book Recommendation System to tailor book suggestions to individual readers' tastes and preferences.</p>

  <h2>Data Files 📂</h2>
  <p>For the Movie Recommendation System, download the following data files and place them in the Movie_data/ folder:</p>
  <ul>
    <li>Recommendor.pkl: Pickle file storing the movie recommendation function.</li>
    <li>df.pkl: Pickle file storing the movie dataset (DataFrame).</li>
    <li>sf.pkl: Pickle file storing the similarity factors for collaborative filtering.</li>
  </ul>
  <p>For the Book Recommendation System, download the following data files and place them in the Book_data/ folder:</p>
  <ul>
    <li>book_df.pkl: Pickle file storing the book dataset (DataFrame).</li>
    <li>sim_fec_book.pkl: Pickle file storing the similarity factors for collaborative filtering of books.</li>
  </ul>

  <h2>Getting Started 🚀</h2>
  <p>Clone the Repository: Begin by cloning this repository to your local machine.</p>
  <p>Install Dependencies: Install the required libraries listed in the requirements.txt file using pip.</p>
  <p>Download Data Files: Follow the instructions in the Data Files section to download the necessary files for both recommendation systems and place them in their respective folders.</p>
  <p>Launch the Apps: Run the Streamlit apps for each recommendation system using the following commands:</p>
  <pre><code>streamlit run Movie_recommender.py</code></pre>
  <pre><code>streamlit run Book_recommender.py</code></pre>
  <p>Discover Movie and Book Gems: Select your favorite movie or book, and our state-of-the-art systems will curate lists of similar titles just for you!</p>

  <h2>Enjoy the Show 🌟</h2>
  <p>Sit back, relax, and enjoy the seamless exploration of fantastic movies and captivating books with our innovative Recommendation System! 🎉</p>

  <h2>Contributions and Feedback 🤝</h2>
  <p>We welcome contributions and feedback to enhance our Recommendation System further. If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.</p>

  <h2>Contact Me 📞</h2>
  <p>Your feedback and suggestions are invaluable to us! Feel free to reach out if you have any questions or want to share your experiences with our Recommendation Systems:</p>
  <ul>
    <li>Email: ashishbaraiya.ce21@sltiet.edu.in</li>
    
  </ul>

  <h2>Discover Movie Gems 🎥</h2>
  <p>Unveil an extraordinary world of cinema by selecting your favorite movie from the dropdown list and receiving personalized movie suggestions based on our advanced recommendation algorithms.</p>

  <h2>Folder Structure 📂</h2>
  <pre>
  ├── movie_recommendation.py
  ├── book_recommendation.py
  ├── Movie_data/
  │   ├── Recommendor.pkl
  │   ├── df.pkl
  │   └── sf.pkl
  ├── Book_data/
  │   ├── book_df.pkl
  │   └── sim_fec_book.pkl
  ├── requirements.txt
  ├── README.md
  ├── LICENSE
  └── link_to_your_logo_image.png (Your project logo, optional)
  </pre>

</body>

</html>
