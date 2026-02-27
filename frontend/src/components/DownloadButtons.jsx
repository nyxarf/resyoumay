export default function DownloadButtons({ result }) {
  if (!result) return null;

  function download(text, filename) {
    const blob = new Blob([text], { type: "text/plain" });
    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    a.click();
  }

  return (
    <div className="downloads">
      <button onClick={() => download(result.resume, "resume.txt")}>
        Download Resume
      </button>

      <button onClick={() => download(result.cover_letter, "cover_letter.txt")}>
        Download Cover Letter
      </button>

      <button
        onClick={() =>
          download(result.portfolio_summary, "portfolio.txt")
        }
      >
        Download Portfolio
      </button>
    </div>
  );
}