import React, { useState } from 'react';
import axios from 'axios';

function UploadForm() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState('');

  const handleFileChange = (e) => {
    const selected = e.target.files[0];
    setFile(selected);
    setPreview(URL.createObjectURL(selected));
    setResult('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

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
        <input type="file" accept="image/*" onChange={handleFileChange} />
        {preview && <img src={preview} alt="Preview" className="image-preview" />}
        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '10px' }}>
          <button type="submit">Deteksi Sekarang</button>
        </div>
      </form>
      {result && <div className="result">{result}</div>}
    </div>
  );
}

export default UploadForm;
