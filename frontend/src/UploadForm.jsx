import React, { useState } from 'react';
import axios from 'axios';

function UploadForm() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState('');
  const [error, setError] = useState('');

  const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png'];

  const handleFileChange = (e) => {
    const selected = e.target.files[0];

    if (selected && allowedTypes.includes(selected.type)) {
      setFile(selected);
      setPreview(URL.createObjectURL(selected));
      setResult('');
      setError('');
    } else {
      setFile(null);
      setPreview(null);
      setResult('');
      setError('Format file tidak didukung. Gunakan gambar .jpg atau .png.');
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError('Silakan pilih file gambar terlebih dahulu.');
      return;
    }

    const formData = new FormData();
    formData.append('image', file);

    try {
      const res = await axios.post('http://localhost:5000/predict', formData);
      setResult(res.data.result || res.data.error);
    } catch (error) {
      console.error('Gagal memprediksi:', error);
      setResult('Terjadi kesalahan saat memproses gambar.');
    }
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <input type="file" accept=".jpg,.jpeg,.png" onChange={handleFileChange} />
        {error && <p style={{ color: 'red' }}>{error}</p>}
        {preview && <img src={preview} alt="Preview" className="image-preview" />}
        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '10px' }}>
          <button type="submit">Deteksi Sekarang</button>
        </div>
      </form>

      {result && <div className="result">{result}</div>}

      {result && result !== 'freshapples' && result !== 'rottenapples' && (
        <p style={{ color: 'orange', fontSize: '0.85em', textAlign: 'center' }}>
          Hasil prediksi mungkin tidak akurat. Pastikan gambar yang diunggah adalah buah apel.
        </p>
      )}


    </div>
  );
}

export default UploadForm;
