import {Chart} from './chart.js';
import {Updates} from './updates.js';

const updateChart = (chart, updates) => async () => {
  const offset = chart.dateOffset();
  const new_data = await updates.get(offset);
  chart.update(new_data);
};

const main = async () => {
  const updates = new Updates();
  const data = await updates.getInitial();
  
  const chart = new Chart(data);
  chart.render();

  setInterval(updateChart(chart, updates), 1000);
};

main();