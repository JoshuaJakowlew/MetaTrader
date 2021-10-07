export class Updates {
  async getInitial () {
    try {
      const res = await axios.get('/updates/init?count=150');
      return res.data;
    } catch (err) {
      console.log(err);
    }
  }

  async get(date_from) {
    try {
      const res = await axios.get(`/updates/get?date_from=${date_from}`);
      return res.data;
    } catch (err) {
      console.log(err);
    }
  }
}