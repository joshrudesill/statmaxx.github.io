
class Symbols {
    constructor(name) {
        this._name = name;
        this._description = "";
        this._mentions = {
            day: {
                total: 0,
                scrapes: []
            },
            week: {
                total: 0,
                scrapes: []
            },
            month: {
                total: 0,
                scrapes: []
            }
        }
    }

    get mentions() {
        return this._mentions;
    }
    get day() {
        return this._mentions.day;
    }
    get week() {
        return this._mentions.week;
    }
    get month() {
        return this._mentions.month;
    }
    get description() {
        return this._description;
    }

    addScrape(mentions, time, source) {
        let scrape = {};
        
        scrape.mentions = mentions;
        scrape.time = time;
        scrape.source = source;

        this._mentions.day.total += mentions;
        this._mentions.day.scrapes.push(scrape); 

        this._mentions.week.total += mentions;
        this._mentions.week.scrapes.push(scrape);

        this._mentions.month.total += mentions;
        this._mentions.month.scrapes.push(scrape);
    }
}



let test = new Symbols("TSLA")

test.addScrape(12,"00:00","Reddit");
test.addScrape(15,"00:10","StockTwits");

console.log(test)
console.log(test.day)

