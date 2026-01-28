from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resumes(resumes, job_desc, max_features=5000):
    tfidf = TfidfVectorizer(max_features=max_features)
    X = tfidf.fit_transform(resumes)

    jd_vec = tfidf.transform([job_desc])
    scores = cosine_similarity(jd_vec, X)[0]

    return scores
