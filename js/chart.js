export class Chart {
  constructor(data) {
    this.data = this.#convertData(data);
    const yBounds = this.#getYBounds(this.data);
    this.chart = this.#createChart(yBounds);
  }

  getData() {
    return this.data;
  }

  dateOffset() {
    return this.data[this.data.length - 1].x.getTime() / 1000;
  }

  render() {
    this.chart.render();
  }

  update(data) {
    data = this.#convertData(data);
    this.data = this.#updatedData(data);   
    this.#updateOptions(this.data);
  }

  #updatedData(data) {
    const leftCut = data.length > 1 ? data.length - 1 : 0;
    const rightCut = this.data.length - 1;
    
    return this.data
      .slice(leftCut, rightCut)
      .concat(data);
  }

  #updateOptions(data) {
    const yBounds = this.#getYBounds(data);
    const options = this.#options(yBounds);

    options.series[0].data = data;

    this.chart.updateOptions(options);
  }

  #convertData(data) {
    return data.map(x => {
      return {
        x: new Date(x.time * 1000),
        y: [x.open, x.high, x.low, x.close],
      }
    });
  }

  #getYBounds(data) {
    return {
      max: data.reduce((prev, cur) => prev.y[1] > cur.y[1] ? prev : cur).y[1],
      min: data.reduce((prev, cur) => prev.y[2] < cur.y[2] ? prev : cur).y[2],
    }
  }

  #createChart(options) {
    return new ApexCharts(document.getElementById('chart'), this.#options(options));
  }

  #options(yBounds) {
    return {
      plotOptions: {
        candlestick: {
          colors: {
            upward: '#346751',
            downward: '#C84B31',
          }
        }
      },
      chart: {
        type: 'candlestick',
        width: '100%',
        height: '100%',
        background: '#161616',
        foreColor: '#ECDBBA',
      },
      series: [{
        name: 'sales',
        data: this.data
      }],
      yaxis: {
        max: yBounds.max,
        min: yBounds.min,
        tooltip: {
          enabled: false,
        },
      },
      xaxis: {
        type: 'datetime',
        tooltip: {
          enabled: false,
        }
      },
    };
  }
}